'use-client'
import { RucioUser } from "@/lib/core/entity/auth-models"
import useUser from "@/lib/infrastructure/hooks/useUser"
import { useRouter } from "next/navigation"
import React from "react"

export type ISessionProps = {
    user: RucioUser
}
const withSession = <P extends {}>(WrappedComponent: React.ComponentType<P & ISessionProps>) => {
    return (props: P) => {
        const router = useRouter()

        const { user } = useUser({
            redirectTo: "/login",
            redirectIfFound: false,
        })


        if (!user || !user.rucioAuthToken) {
            router.push('/login')
            return null
        }

        const WrappedComponentWithSession = (props: P) => {
            // At this point, the props being passed in are the original props the component expects.
            return <WrappedComponent user={user} {...props}/>;
        };

        return WrappedComponentWithSession;
    }
}

export default withSession